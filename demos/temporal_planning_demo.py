"""
Demo: How different cognitive architectures approach temporal planning
"""

from tide.examples.temporal_planning import TemporalPlanningTask

def main():
    print("=== TIDE Framework: Temporal Planning Demo ===\n")
    
    # Create planners for each architecture
    architectures = ['NT', 'ASD', 'ADHD']
    
    for arch_type in architectures:
        print(f"\n{arch_type} Architecture Planning:")
        print("-" * 50)
        
        planner = TemporalPlanningTask(arch_type)
        week_plan = planner.plan_week()
        
        # Display the plan
        for day, activities in week_plan.items():
            print(f"\n{day}:")
            for activity in activities:
                print(f"  - {activity}")
        
        # Show consistency metric
        consistency = planner.evaluate_plan_consistency()
        print(f"\nPlan consistency across 4 weeks: {consistency:.2f}")

if __name__ == "__main__":
    main()
