"""
Demonstration of how different cognitive architectures approach temporal planning.
Clear behavioral differences emerge from dimensional organization patterns.
"""

import numpy as np
from typing import List, Dict
from datetime import datetime, timedelta
from ..core.architecture import CognitiveArchitecture

class TemporalPlanningTask:
    """
    Task: Plan a sequence of activities over a week.
    Each architecture will show distinct planning strategies.
    """
    
    def __init__(self, architecture_type: str):
        self.architecture = CognitiveArchitecture(architecture_type)
        self.activities = [
            'work', 'exercise', 'social', 'rest', 'creative', 'chores'
        ]
    
    def plan_week(self) -> Dict[str, List[str]]:
        """
        Generate a week plan based on architecture type.
        
        Returns:
            Dictionary mapping days to planned activities
        """
        if self.architecture.type == 'NT':
            return self._flexible_planning()
        elif self.architecture.type == 'ASD':
            return self._systematic_planning()
        elif self.architecture.type == 'ADHD':
            return self._immediate_planning()
    
    def _flexible_planning(self) -> Dict[str, List[str]]:
        """NT: Create flexible plan with room for adjustment"""
        plan = {}
        base_schedule = {
            'Monday': ['work', 'exercise', 'rest'],
            'Tuesday': ['work', 'creative', 'social'],
            'Wednesday': ['work', 'chores', 'rest'],
            'Thursday': ['work', 'exercise', 'creative'],
            'Friday': ['work', 'social', 'rest'],
            'Saturday': ['chores', 'creative', 'social'],
            'Sunday': ['rest', 'exercise', 'creative']
        }
        
        # Add flexibility markers
        for day, activities in base_schedule.items():
            plan[day] = activities + ['*flexible time*']
        
        return plan
    
    def _systematic_planning(self) -> Dict[str, List[str]]:
        """ASD: Create detailed, systematic plan with specific times"""
        plan = {}
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday', 'Sunday']
        
        # Create rigid rotating schedule
        activity_rotation = [
            ['9:00-work', '14:00-exercise', '18:00-rest', '20:00-creative'],
            ['9:00-work', '14:00-chores', '18:00-social', '20:00-rest'],
            ['9:00-work', '14:00-creative', '18:00-exercise', '20:00-rest']
        ]
        
        for i, day in enumerate(days):
            plan[day] = activity_rotation[i % 3].copy()
            # Add specific break times
            plan[day].insert(2, '12:00-lunch break (30 min)')
        
        return plan
    
    def _immediate_planning(self) -> Dict[str, List[str]]:
        """ADHD: Plan only for 'today', everything else is vague"""
        plan = {}
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday', 'Sunday']
        
        # Detailed plan for "today" only
        today_activities = np.random.choice(self.activities, 3, replace=False)
        plan['TODAY'] = [f"NOW: {today_activities[0]}", 
                        f"Maybe later: {today_activities[1]}", 
                        f"If time: {today_activities[2]}"]
        
        # Vague plans for other days
        for day in days[1:]:
            plan[day] = ['probably something', 'will figure it out']
        
        return plan
    
    def evaluate_plan_consistency(self, num_weeks: int = 4) -> float:
        """
        Measure how consistent plans are across multiple weeks.
        ASD should show highest consistency.
        """
        plans = [self.plan_week() for _ in range(num_weeks)]
        
        # Simple consistency metric: how similar are the plans?
        consistency_scores = []
        for i in range(1, num_weeks):
            similarity = self._compare_plans(plans[0], plans[i])
            consistency_scores.append(similarity)
        
        return np.mean(consistency_scores)
    
    def _compare_plans(self, plan1: Dict, plan2: Dict) -> float:
        """Compare two weekly plans for similarity"""
        total_similarity = 0
        days_compared = 0
        
        for day in plan1:
            if day in plan2:
                # Calculate Jaccard similarity for activities
                set1 = set(plan1[day])
                set2 = set(plan2[day])
                if len(set1.union(set2)) > 0:
                    similarity = len(set1.intersection(set2)) / len(set1.union(set2))
                    total_similarity += similarity
                    days_compared += 1
        
        return total_similarity / days_compared if days_compared > 0 else 0
