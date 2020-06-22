import csv

def save_to_file(jobs, filename):
    with open(f'jobs/{filename}.csv', mode='w', newline='') as file:
        fieldnames = ['title', 'company', 'location', 'link']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for job in jobs:
            writer.writerow(job)
    

