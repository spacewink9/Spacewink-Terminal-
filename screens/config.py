class AdvanceSettings:
    def __init__(self, analysis_type, use_machine_learning, portfolio_optimization, risk_analysis):
        self.analysis_type = analysis_type
        self.use_machine_learning = use_machine_learning
        self.portfolio_optimization = portfolio_optimization
        self.risk_analysis = risk_analysis

    def get_analysis_type(self):
        return self.analysis_type

    def set_analysis_type(self, analysis_type):
        self.analysis_type = analysis_type

    def use_machine_learning(self):
        return self.use_machine_learning

    def enable_machine_learning(self):
        self.use_machine_learning = True

    def disable_machine_learning(self):
        self.use_machine_learning = False

    def use_portfolio_optimization(self):
        return self.portfolio_optimization

    def enable_portfolio_optimization(self):
        self.portfolio_optimization = True

    def disable_portfolio_optimization(self):
        self.portfolio_optimization = False

    def use_risk_analysis(self):
        return self.risk_analysis

    def enable_risk_analysis(self):
        self.risk_analysis = True

    def disable_risk_analysis(self):
        self.risk_analysis = False
