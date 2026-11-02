import pandas as pd
import matplotlib.pyplot as plt

roles = [
    'Data Analyst',
    'Data Engineer',
    'Data Scientist',
    'ML Engineer',
    'Business Analyst'
]

counts = [300, 500, 450, 200, 150]

df = pd.DataFrame({
    'Role': roles,
    'Count': counts
})

print("DISTRIBUTION OF DATA SCIENCE ROLES")
print(df)

plt.figure(figsize=(10, 6))
plt.bar(roles, counts)

plt.title('Distribution of Data Science Roles')
plt.xlabel('Role')
plt.ylabel('Count')
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig('Experiment-01/outputs/1b_job_roles.png')
plt.show()
