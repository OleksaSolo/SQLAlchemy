import logging

import my_select


package_name="hw"
logger = logging.getLogger(package_name)

if __name__ == "__main__":
    for task in my_select.get_tasks():
        print("-" * 80)
        print(task.__name__)
        task_result = task()
        if task_result:
            column_names = task_result.get("column_names")
            print(".   " * 20)
            for id, row in enumerate(task_result.get("result")):
                row_str = []
                for i, col in enumerate(row):
                    row_str.append(f'{column_names[i]}: "{col}"')
                result = ", ".join(row_str)
                print(f"[{id+1:2}] {result}")
