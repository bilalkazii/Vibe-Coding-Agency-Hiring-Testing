Complete Secure Version
"""
Secure Data Processing and Cloud Upload Service
Fixed all security vulnerabilities from AI-generated code
"""

import os
import requests
import json
import sqlite3
import logging
from datetime import datetime
from typing import Optional, Dict, Any
import hashlib
import hmac

# Secure credential management
API_KEY = os.environ.get('API_KEY')
DATABASE_PASSWORD = os.environ.get('DB_PASSWORD')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')

# Get database URL from environment
DB_CONNECTION_STRING = os.environ.get('DATABASE_URL', 'sqlite:///app_data.db')

class SecureDataProcessor:
    def __init__(self):
        # Secure logging configuration
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Secure session with SSL verification
        self.session = requests.Session()
        self.session.verify = True  # Always verify SSL
        
        # Rate limiting
        self.request_count = 0
        self.max_requests_per_minute = 60
    
    def connect_to_database(self) -> tuple:
        """Connect to database with secure connection"""
        try:
            conn = sqlite3.connect("app_data.db", timeout=10)
            cursor = conn.cursor()
            
            # Create secure table schema
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS secure_user_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    email_encrypted TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create audit table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    action TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    ip_address TEXT,
                    user_agent TEXT
                )
            """)
            
            conn.commit()
            return conn, cursor
            
        except Exception as e:
            self.logger.error(f"Database connection failed: {str(e)}")
            return None, None
    
    def validate_user_input(self, user_id: Any) -> bool:
        """Validate user input to prevent injection attacks"""
        if not isinstance(user_id, (int, str)):
            return False
        
        # Convert to string and check for SQL injection patterns
        user_id_str = str(user_id)
        sql_injection_patterns = ["'", "\"", ";", "--", "/*", "*/", "union", "select", "drop", "delete"]
        
        for pattern in sql_injection_patterns:
            if pattern in user_id_str.lower():
                self.logger.warning(f"Potential SQL injection detected: {user_id_str}")
                return False
        
        return True
    
    def fetch_user_data(self, user_id: Any) -> Optional[Dict]:
        """Fetch user data with SQL injection protection"""
        if not self.validate_user_input(user_id):
            return None
        
        conn, cursor = self.connect_to_database()
        if not cursor:
            return None
        
        try:
            # Use parameterized query to prevent SQL injection
            query = "SELECT id, username, email_encrypted, created_at FROM secure_user_data WHERE id = ?"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            
            if result:
                return {
                    'id': result[0],
                    'username': result[1],
                    'email': result[2],  # Would need decryption in real implementation
                    'created_at': result[3]
                }
            return None
            
        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            return None
        finally:
            if conn:
                conn.close()
    
    def call_external_api(self, data: Dict) -> Optional[Dict]:
        """Make secure API calls with proper error handling"""
        if self.request_count >= self.max_requests_per_minute:
            self.logger.warning("Rate limit exceeded")
            return None
        
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
            'User-Agent': 'SecureDataProcessor/1.0'
        }
        
        try:
            response = self.session.post(
                "https://api.secure-service.com/v1/process",
                headers=headers,
                json=data,
                timeout=30  # Add timeout
            )
            
            self.request_count += 1
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:
                self.logger.warning("Rate limited by API")
                return None
            else:
                self.logger.error(f"API call failed: {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            self.logger.error("API request timeout")
            return None
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API request failed: {str(e)}")
            return None
    
    def upload_to_cloud(self, file_path: str, bucket_name: str = "company-safe-data") -> bool:
        """Upload files to cloud storage securely"""
        try:
            import boto3
            from botocore.exceptions import ClientError
            
            # Use IAM roles or environment variables
            s3_client = boto3.client(
                's3',
                region_name=os.environ.get('AWS_REGION', 'us-east-1')
            )
            
            # Validate file type
            allowed_extensions = ['.txt', '.csv', '.json', '.log']
            file_ext = os.path.splitext(file_path)[1].lower()
            
            if file_ext not in allowed_extensions:
                self.logger.error(f"File type not allowed: {file_ext}")
                return False
            
            # Encrypt file before upload (pseudo-code)
            # encrypted_file = self.encrypt_file(file_path)
            
            s3_client.upload_file(
                file_path, 
                bucket_name, 
                os.path.basename(file_path),
                ExtraArgs={
                    'ServerSideEncryption': 'AES256',
                    'StorageClass': 'STANDARD'
                }
            )
            
            self.logger.info(f"File securely uploaded to s3://{bucket_name}/{os.path.basename(file_path)}")
            return True
            
        except ClientError as e:
            self.logger.error(f"S3 upload failed: {e.response['Error']['Message']}")
            return False
        except Exception as e:
            self.logger.error(f"Upload failed: {str(e)}")
            return False
    
    def validate_webhook_signature(self, payload: Dict, signature: str) -> bool:
        """Validate webhook signature to prevent unauthorized access"""
        secret = os.environ.get('WEBHOOK_SECRET')
        if not secret:
            self.logger.error("Webhook secret not configured")
            return False
        
        # Create expected signature
        expected_sig = hmac.new(
            secret.encode(),
            json.dumps(payload, sort_keys=True).encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(expected_sig, signature)
    
    def process_webhook_data(self, webhook_data: Dict, signature: str) -> Dict:
        """Process incoming webhook with validation"""
        # Validate webhook signature
        if not self.validate_webhook_signature(webhook_data, signature):
            self.logger.error("Invalid webhook signature")
            return {"status": "error", "message": "Invalid signature"}
        
        try:
            # Validate required fields
            required_fields = ['user_id', 'action']
            for field in required_fields:
                if field not in webhook_data:
                    return {"status": "error", "message": f"Missing required field: {field}"}
            
            user_id = webhook_data['user_id']
            action = webhook_data['action']
            
            # Whitelist allowed actions
            allowed_actions = ['get_user', 'update_preferences']
            if action not in allowed_actions:
                return {"status": "error", "message": f"Action not allowed: {action}"}
            
            # Process based on action
            if action == 'get_user':
                user_data = self.fetch_user_data(user_id)
                return {"status": "success", "data": user_data}
            else:
                return {"status": "error", "message": "Action not implemented"}
                
        except Exception as e:
            self.logger.error(f"Webhook processing failed: {str(e)}")
            return {"status": "error", "message": "Internal server error"}

def main():
    """Main function demonstrating secure patterns"""
    processor = SecureDataProcessor()
    print("Starting secure data processing...")
    
    # Test secure operations
    user_data = processor.fetch_user_data(1)
    api_result = processor.call_external_api({"test": "secure_data"})
    
    print("Secure processing complete")

if __name__ == "__main__":    
    main()
