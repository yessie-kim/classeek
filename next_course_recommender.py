import pandas as pd

def recommend_course(courses_taken, course_type, num_to_recommend):
    
    course_list = pd.read_csv('next_course_recommender_df.csv')
    
    valid_requirement_dist_options = course_list['Course List Description'].unique().tolist()
    
    if courses_taken in course_list['Subject/Catalog'].tolist():
    
        type_of_course = df[df['Subject/Catalog'] == courses_taken]['Course List Description'].values[0]
        course_requirement = df[df['Subject/Catalog'] == courses_taken]['Require']
        course_requirement_of_type = df[df['Course List Description'] == course_type]['Require']

        # If the course entered belongs to the "One" list
        if course_requirement.any() == 'One':
            print(f'The requirement distribution of {courses_taken} is {type_of_course}.')
            print(f'You only need to take one course of the {type_of_course} requirement.')
            print(f'You have fully met the {type_of_course} requirement.')

        # If not
        elif course_requirement.any() != 'One':
            
            # If the type entered is not on the list
            if course_type not in course_list['Course List Description'].tolist():
                print('Requirement distribution not found')
            
            # If it does
            elif course_type in course_list['Course List Description'].tolist():

                # If the type of the course entered and the course type entered are not the same
                if type_of_course != course_type:

                    print('These courses are not of the same requirement')
                    print('----------------------')

                    print(f'The requirement distribution of {courses_taken} is {type_of_course}.')
                    print(f'Recommending courses of the same requirement with {courses_taken}:')
                    courses_of_same_type_entered = df[df['Course List Description'] == type_of_course]
                    courses_not_taken_entered = courses_of_same_type_entered[courses_of_same_type_entered['Subject/Catalog'] != courses_taken][['Subject/Catalog', 'Course Title']]

                    # If the number of course in list is longer than num_to_recommend
                    if len(courses_not_taken_entered) <  num_to_recommend:
                        courses_to_recommend_entered = courses_not_taken_entered[['Subject/Catalog', 'Course Title']]
                        print(f'Total number of recommendations: {len(courses_to_recommend_entered)}')

                    # If the number of course in list is shorter than num_to_recommend
                    else:
                        courses_to_recommend_entered = courses_not_taken_entered.sample(num_to_recommend)[['Subject/Catalog', 'Course Title']]
                        print(f'Total number of recommendations: {len(courses_to_recommend_entered)}')

                    print(courses_to_recommend_entered)
                    print('----------------------')

                    print(f'Recommending course of the {course_type} requirement:')
                    courses_of_same_type = df[df['Course List Description'] == course_type]
                    courses_not_taken = courses_of_same_type[courses_of_same_type['Subject/Catalog'] != courses_taken][['Subject/Catalog', 'Course Title']]

                    # If the number of course in list is longer than num_to_recommend
                    if len(courses_not_taken) <  num_to_recommend:
                        courses_to_recommend = courses_not_taken[['Subject/Catalog', 'Course Title']]
                        print(f'Total number of recommendations: {len(courses_to_recommend)}')

                    # If the number of course in list is shorter than num_to_recommend
                    else:
                        courses_to_recommend = courses_not_taken.sample(num_to_recommend)[['Subject/Catalog', 'Course Title']]
                        print(f'Total number of recommendations: {len(courses_to_recommend)}')

                    print(courses_to_recommend)

                ###########################################

            else:
                # If the type of the course entered and the course type entered are the same
                print(f'Course {courses_taken} is of {course_type} requirement.')
                print(f'Recommending course of the {course_type} requirement:')
                courses_of_same_type = df[df['Course List Description'] == course_type]
                courses_not_taken = courses_of_same_type[courses_of_same_type['Subject/Catalog'] != courses_taken][['Subject/Catalog', 'Course Title']]

                # If the number of course in list is longer than num_to_recommend
                if len(courses_not_taken) <  num_to_recommend:
                    courses_to_recommend = courses_not_taken[['Subject/Catalog', 'Course Title']]
                    print(f'Total number of recommendations: {len(courses_to_recommend)}')

                # If the number of course in list is shorter than num_to_recommend
                else:
                    courses_to_recommend = courses_not_taken.sample(num_to_recommend)[['Subject/Catalog', 'Course Title']]
                    print(f'Total number of recommendations: {len(courses_to_recommend)}')

                print(courses_to_recommend)
                
    else:
        print('Course not found')