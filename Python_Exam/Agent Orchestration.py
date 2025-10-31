QUESTION 1: AGENT DESIGN
"""
AGENT ORCHESTRATION FOR CLOUD ARCHITECTURE PLANNING
"""

class CloudArchitectureOrchestrator:
    def __init__(self):
        self.agents = {
            'requirements_analyst': RequirementsAnalyst(),
            'architecture_designer': ArchitectureDesigner(), 
            'cloud_specialist': CloudSpecialist(),
            'cost_optimizer': CostOptimizer(),
            'security_reviewer': SecurityReviewer()
        }

class RequirementsAnalyst:
    """Agent 1: Business Requirements to Technical Needs"""
    
    def analyze(self, problem_description: str, business_context: dict) -> dict:
        """
        Input: Problem description + business context
        Output: Technical requirements, constraints, expected load
        """
        return {
            'functional_requirements': [],
            'non_functional_requirements': {},
            'expected_load': {},
            'compliance_needs': [],
            'integration_requirements': []
        }

class ArchitectureDesigner:
    """Agent 2: Technical Requirements to Architecture"""
    
    def design(self, requirements: dict) -> dict:
        """
        Input: Technical requirements from RequirementsAnalyst
        Output: High-level architecture diagram and components
        """
        return {
            'architecture_type': '',  # microservices, serverless, etc.
            'components': [],
            'data_flow': {},
            'scaling_strategy': ''
        }

class CloudSpecialist:
    """Agent 3: Architecture to Cloud Services"""
    
    def recommend_services(self, architecture: dict, cloud_provider: str = 'aws') -> dict:
        """
        Input: Architecture design + cloud provider preference
        Output: Specific cloud services recommendations
        """
        return {
            'compute_services': [],
            'storage_services': [], 
            'networking_services': [],
            'database_services': [],
            'security_services': []
        }

class CostOptimizer:
    """Agent 4: Cost Optimization"""
    
    def optimize(self, services: dict, budget: float) -> dict:
        """
        Input: Cloud services + budget constraints
        Output: Cost-optimized architecture with pricing
        """
        return {
            'monthly_cost_estimate': 0.0,
            'cost_optimization_suggestions': [],
            'reserved_instances_recommendations': [],
            'monitoring_cost_alerts': []
        }

class SecurityReviewer:
    """Agent 5: Security and Compliance"""
    
    def review(self, architecture: dict, services: dict) -> dict:
        """
        Input: Architecture + cloud services
        Output: Security assessment and improvements
        """
        return {
            'security_risks': [],
            'compliance_gaps': [],
            'security_improvements': [],
            'encryption_recommendations': []
        }


QUESTION 2: ORCHESTRATION WORKFLOW (E-commerce Scenario)
def ecommerce_orchestration_workflow():
    """
    Complete workflow for E-commerce Site scenario
    """
    orchestrator = CloudArchitectureOrchestrator()
    
    # Step 1: Requirements Analysis
    problem = "Simple E-commerce Site: Online store for small business (1000 daily users), Product catalog, shopping cart, payment processing, Basic admin dashboard"
    
    print("🎯 STEP 1: Requirements Analysis")
    requirements = orchestrator.agents['requirements_analyst'].analyze(
        problem, 
        {'budget': 'medium', 'team_size': 'small', 'time_to_market': 'fast'}
    )
    
    # Error handling for requirements analysis
    if not requirements.get('functional_requirements'):
        print("⚠️  Requirements analysis failed - using default template")
        requirements = get_default_ecommerce_requirements()
    
    # Step 2: Architecture Design  
    print("🏗️  STEP 2: Architecture Design")
    architecture = orchestrator.agents['architecture_designer'].design(requirements)
    
    # Validate architecture feasibility
    if not architecture.get('components'):
        print("❌ Architecture design failed - escalating to human architect")
        return None
    
    # Step 3: Cloud Service Selection
    print("☁️  STEP 3: Cloud Service Mapping")
    services = orchestrator.agents['cloud_specialist'].recommend_services(
        architecture, 'aws'
    )
    
    # Step 4: Cost Optimization
    print("💰 STEP 4: Cost Optimization") 
    optimized_plan = orchestrator.agents['cost_optimizer'].optimize(
        services, budget=500  # $500/month budget
    )
    
    # Step 5: Security Review
    print("🔒 STEP 5: Security Review")
    security_assessment = orchestrator.agents['security_reviewer'].review(
        architecture, services
    )
    
    # Final Integration
    final_recommendation = {
        'requirements': requirements,
        'architecture': architecture,
        'services': services,
        'cost_optimization': optimized_plan,
        'security': security_assessment,
        'implementation_priority': ['compute', 'database', 'authentication', 'payment']
    }
    
    return final_recommendation

def get_default_ecommerce_requirements():
    """Fallback requirements template"""
    return {
        'functional_requirements': [
            'user_registration_login',
            'product_catalog_browsing', 
            'shopping_cart_management',
            'payment_processing',
            'order_management',
            'admin_dashboard'
        ],
        'non_functional_requirements': {
            'availability': '99.9%',
            'response_time': '<2 seconds',
            'concurrent_users': 1000
        }
    }

QUESTION 3: CLOUD RESOURCE MAPPING
def ecommerce_cloud_resource_mapping():
    """
    Cloud services recommendation for E-commerce scenario
    """
    return {
        'compute': {
            'services': ['AWS Lambda', 'Amazon EC2'],
            'justification': 'Lambda for serverless APIs, EC2 for admin dashboard',
            'scaling': 'Auto Scaling Groups for EC2, automatic for Lambda'
        },
        'storage': {
            'databases': [
                {'service': 'Amazon DynamoDB', 'purpose': 'user_sessions_cart'},
                {'service': 'Amazon RDS PostgreSQL', 'purpose': 'product_catalog_orders'}
            ],
            'file_storage': [
                {'service': 'Amazon S3', 'purpose': 'product_images_static_assets'}
            ],
            'caching': [
                {'service': 'Amazon ElastiCache Redis', 'purpose': 'product_catalog_cache'}
            ]
        },
        'networking': {
            'api_gateway': 'Amazon API Gateway',
            'load_balancer': 'Application Load Balancer',
            'cdn': 'Amazon CloudFront',
            'domain_management': 'Amazon Route 53'
        },
        'security': {
            'authentication': 'Amazon Cognito',
            'waf': 'AWS WAF',
            'encryption': 'AWS KMS',
            'monitoring': 'AWS CloudTrail + Amazon GuardDuty'
        },
        'monitoring': {
            'logging': 'Amazon CloudWatch Logs',
            'metrics': 'Amazon CloudWatch Metrics',
            'alerts': 'Amazon CloudWatch Alarms',
            'tracing': 'AWS X-Ray'
        }
    }

QUESTION 4: REUSABILITY & IMPROVEMENT
class ReusableOrchestrationSystem:
    """
    System designed for reusability across different projects
    """
    
    def __init__(self):
        self.learned_patterns = {}
        self.project_templates = {}
        self.feedback_mechanism = FeedbackCollector()
    
    def standardize_components(self):
        """Standardized components across all projects"""
        return {
            'authentication': ['Cognito', 'Auth0', 'Azure AD'],
            'database': ['DynamoDB', 'RDS', 'Firestore'],
            'compute': ['Lambda', 'EC2', 'Container'],
            'monitoring': ['CloudWatch', 'Datadog', 'NewRelic']
        }
    
    def customize_per_project(self, project_type: str):
        """Project-specific customizations"""
        templates = {
            'ecommerce': {
                'must_have': ['payment_processing', 'inventory_management'],
                'performance_focus': ['catalog_search', 'checkout_flow']
            },
            'chatbot': {
                'must_have': ['nlp_processing', 'conversation_state'],
                'performance_focus': ['response_time', 'concurrent_sessions']
            },
            'mobile_app': {
                'must_have': ['offline_support', 'push_notifications'],
                'performance_focus': ['battery_usage', 'data_sync']
            }
        }
        return templates.get(project_type, {})
    
    def learn_from_previous(self, project_history: list):
        """Learn from past project successes and failures"""
        for project in project_history:
            if project['success_metrics']['uptime'] > 99.9:
                self.learned_patterns['high_availability'] = project['architecture']
            
            if project['cost_metrics']['savings'] > 0.2:  # 20% savings
                self.learned_patterns['cost_optimization'] = project['cost_strategies']
    
    def collect_feedback(self, project_result: dict):
        """Continuous improvement through feedback"""
        self.feedback_mechanism.submit_feedback({
            'project_type': project_result['type'],
            'success_factors': project_result['success_factors'],
            'pain_points': project_result['pain_points'],
            'developer_satisfaction': project_result['satisfaction_score']
        })

class FeedbackCollector:
    """Collect and analyze feedback for system improvement"""
    
    def __init__(self):
        self.feedback_data = []
        self.improvement_suggestions = []
    
    def submit_feedback(self, feedback: dict):
        self.feedback_data.append(feedback)
        self.analyze_feedback_patterns()
    
    def analyze_feedback_patterns(self):
        """Analyze feedback to identify common patterns"""
        if len(self.feedback_data) > 10:
            # Identify common success factors
            common_success = self._find_common_elements(
                [f['success_factors'] for f in self.feedback_data]
            )
            
            # Identify common pain points
            common_pain_points = self._find_common_elements(
                [f['pain_points'] for f in self.feedback_data]
            )
            
            self.improvement_suggestions = self._generate_improvements(
                common_success, common_pain_points
            )

QUESTION 5: PRACTICAL CONSIDERATIONS
class ChallengeHandler:
    """
    Handle practical challenges in agent orchestration
    """
    
    def handle_conflicting_recommendations(self, agent_recommendations: dict):
        """
        Resolve conflicts between agent recommendations
        """
        conflicts = self._identify_conflicts(agent_recommendations)
        
        resolution_strategy = {
            'security_vs_cost': 'Prioritize security with cost compromises',
            'performance_vs_complexity': 'Balance based on project criticality',
            'innovation_vs_stability': 'Choose stability for production systems'
        }
        
        resolved = {}
        for conflict_type, recommendations in conflicts.items():
            if conflict_type in resolution_strategy:
                resolved[conflict_type] = self._apply_resolution_strategy(
                    recommendations, resolution_strategy[conflict_type]
                )
        
        return resolved
    
    def handle_vague_requirements(self, problem_statement: str):
        """
        Handle incomplete or vague problem statements
        """
        clarification_questions = [
            "What is the expected user load?",
            "What is the budget range?",
            "Any specific compliance requirements?",
            "Integration with existing systems?",
            "Team's technical expertise level?"
        ]
        
        # Use AI to generate specific questions based on problem type
        if 'ecommerce' in problem_statement.lower():
            clarification_questions.extend([
                "Payment processor preferences?",
                "Inventory management needs?",
                "Shipping integration requirements?"
            ])
        
        return {
            'status': 'needs_clarification',
            'clarification_questions': clarification_questions,
            'assumptions_made': self._make_conservative_assumptions(problem_statement)
        }
    
    def handle_budget_constraints(self, services: dict, hidden_budget: float):
        """
        Adjust recommendations based on unstated budget constraints
        """
        cost_optimized_services = {}
        
        for category, service_list in services.items():
            cost_optimized_services[category] = []
            
            for service in service_list:
                affordable_service = self._find_affordable_alternative(
                    service, hidden_budget
                )
                cost_optimized_services[category].append(affordable_service)
        
        return cost_optimized_services
    
    def handle_legacy_integration(self, new_architecture: dict, legacy_systems: list):
        """
        Integrate with existing legacy systems
        """
        integration_strategy = {
            'api_gateway': 'Use API Gateway as facade for legacy APIs',
            'data_migration': 'Gradual migration with dual-write strategy',
            'authentication': 'Federated identity between new and legacy systems'
        }
        
        return {
            'integration_approach': 'strangler_pattern',
            'migration_phases': self._create_migration_plan(new_architecture, legacy_systems),
            'risk_mitigation': 'circuit_breaker_pattern_for_legacy_calls'
        }
    
    def keep_updated_cloud_services(self):
        """
        Stay current with new cloud services and pricing
        """
        update_strategy = {
            'continuous_learning': 'Monthly review of cloud provider updates',
            'pricing_monitoring': 'Automated cost optimization recommendations',
            'service_evaluation': 'Quarterly assessment of new services',
            'community_input': 'Leverage cloud community feedback'
        }
        
        return update_strategy
