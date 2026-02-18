class TemplateInjector:

    def __init__(self, template, items):
        self.template = template
        self.items = items

    def inject(self):
        for item in self.items.strip().split("\n"):
            if item.strip():   # skip empty lines
                print(self.template + item)
                print('*'*100)


def main():
    items = '''
| 1    | Goal Clarity            | Define 1-year, 3-month, weekly direction clearly | You stop reacting and start directing your effort |
| 2    | Impact Thinking         | Measure work by outcome, not effort              | You choose leverage over busyness                 |
| 3    | Opportunity Cost        | Every choice kills alternatives                  | You stop wasting time subconsciously              |
| 4    | Important vs Urgent     | Distinguish long-term drivers from noise         | You control your schedule instead of reacting     |
| 5    | Leverage Identification | Find actions that unlock many future benefits    | You invest in compounding skills                  |
| 6    | Constraint Awareness    | Identify bottlenecks limiting growth             | You work on what actually increases throughput    |
| 7    | Energy Management       | Align hard tasks with peak mental hours          | Output increases without burnout                  |
| 8    | ROI Scoring             | Score tasks based on impact vs effort            | Decisions become objective, not emotional         |
| 9    | Compounding Effect      | Prioritize skills that stack long-term           | You build unfair advantage                        |
| 10   | Elimination Skill       | Ruthlessly cut low-value tasks                   | Cognitive load reduces drastically                |
| 11   | Deep Work Discipline    | Protect uninterrupted focus blocks               | Quality and speed improve massively               |
| 12   | Weekly Review System    | Reflect → Adjust → Optimize                      | Continuous improvement becomes automatic          |
'''

    template = "Hey hi, I am weak at time management , and priortize tasks with limited time , so which causes me to pay worst opportunity costs so I want to master it i am at "

    injector = TemplateInjector(template, items)
    injector.inject()


if __name__ == "__main__":
    main()
