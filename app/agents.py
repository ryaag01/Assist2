# app/agents.py

class BaseAgent:
    def process(self, task: str) -> str:
        raise NotImplementedError("Each agent must implement its own process method.")

class DeveloperAgent(BaseAgent):
    def process(self, task: str) -> str:
        return f"DeveloperAgent: Code generated for task '{task}'."

class TesterAgent(BaseAgent):
    def process(self, task: str) -> str:
        return f"TesterAgent: Testing completed for '{task}'."

class ResearcherAgent(BaseAgent):
    def process(self, task: str) -> str:
        return f"ResearcherAgent: Research data collected for '{task}'."

class DataManagerAgent(BaseAgent):
    def process(self, task: str) -> str:
        return f"DataManagerAgent: Data processed for '{task}'."

class ECommerceAgent(BaseAgent):
    def process(self, task: str) -> str:
        return f"ECommerceAgent: E-commerce strategies updated for '{task}'."

class MarketingAgent(BaseAgent):
    def process(self, task: str) -> str:
        return f"MarketingAgent: Marketing analysis done for '{task}'."

class BizDevAgent(BaseAgent):
    def process(self, task: str) -> str:
        return f"BizDevAgent: Business opportunities evaluated for '{task}'."
