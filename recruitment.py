


def get_skills():
    return ["programming", "human resources", "advertising"]
    # Add at least 3 random skills for the user to select from
    


def show_skills(skills):
   print()
   print ("Skills:")
   
   for idx, skill in enumerate (skills, start=1):
       print(f"{idx}. {skill}")
       
   print()
    
    # Pretty print skills to the user
    # Write your code here



def get_user_skills(skills):
    show_skills(skills)
    chosen_skills = [
        input("choose a skill from above by entering its number:"),
        input("choose another skill from above by entering its number:"),
    ]
    return [skills[int(selected)-1]for selected in chosen_skills]
    # Show the available skills and have user pick from them
    # Write your code here
    ...


def get_user_cv(skills):
    return{"name": input("what is your name"),
           "age": int(input("how old are you?")),
           "experience": int(input("how many years of experience do you have?")),
           "skills": get_user_skills(skills),
           }
    # Get the users CV from their inputs
    # Write your code here
    ...


def check_acceptance(cv, desired_skill):
    return(
        25< cv["age"]<40
        and cv["experience"]>3
        and desired_skill in cv ["skills"]
    )

def main():
    print("welcome to the recruitment program, please answer the following questions:")
    skills = get_skills()
    wanted_skills=2
    
    cv = get_user_cv(skills)
    
    if check_acceptance(cv, skills[wanted_skills]):
        print((f"you have been accepted, {cv['name']}."))
    else:
        print("sorry you have been rejected.")

if __name__ == "__main__":
    main()
