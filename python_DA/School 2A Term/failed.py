# https://leetcode.com/problems/triangle/


#         path_curr = min(triangle[0])
#         pos = triangle[0].index(path_curr)

#         for row in triangle[1:]:
#             print(min([row[pos], row[pos+1]]))
#             path_curr = path_curr + min([row[pos], row[pos+1]])
#         return path_curr

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return

        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]


# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

def find_match (point, points):
    unmatched =[]
    for location in points:
        if (point[0] >= location[0] and point[0] <= location[1]) or (point[1] >= location[0] and point[1] <= location[1]) or (point[0] <= location[0] and point[1] >= location[1]) or (point[0] >= location[0] and point[1] <= location[1]):
            continue
        else:
            unmatched.append(location)
    return unmatched



    # if not points:
    #     print(points)
    #     print(unmatched)
    #     ans = unmatched
    #     return ans
    # elif (point[0] >= points[0][0] and point[0] <= points[0][1]) or (point[1] >= points[0][0] and point[1] <= points[0][1]) or (point[0] <= points[0][0] and point[1] >= points[0][1]) or (point[0] >= points[0][0] and point[1] <= points[0][1]):
    #     print(unmatched)
    #     print(points[0])
    #     find_match (point, points[1:], unmatched)
    # else:
    #     print(unmatched)
    #     print([points[0],1])
    #     find_match (point, points[1:], unmatched + [points[0]])


minArrows = 0
def min_arraows (points):
    if not points:
        return minArrows
    else:
        minArrows = minArrows + 1
        min_arraows (find_match (points[0], points[1:]))

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return min_arraows (points)






# https://leetcode.com/problems/course-schedule/

def noOverlap(dependancies):
    for coursePos in dependancies:
        for course in dependancies[coursePos]:
            if coursePos in dependancies[course]:
                return False
    return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependancies = {}
        # course_used = 0
        for courses in prerequisites:
            if courses[0] == courses[1]:
                return False
            elif (courses[0] in dependancies) and (courses[1] in dependancies):
                dependancies[courses[0]] = dependancies[courses[0]] + [courses[1]]
            elif (courses[0] in dependancies):
                dependancies[courses[0]] = dependancies[courses[0]] + [courses[1]]
                dependancies[courses[1]] = []
            elif (courses[1] in dependancies):
                dependancies[courses[0]] = [courses[1]]
            else:
                dependancies[courses[0]] = [courses[1]]
                dependancies[courses[1]] = []
        print(dependancies)
        if (len(dependancies) <= numCourses) and noOverlap(dependancies):
            return True
        else:
            return False












        # return dependancies

#             if (courses[1] in dependancies) and (courses[0] in dependancies):
#                 dependancies[courses[0]] = dependancies[courses[0]] + [courses[1]]
#             elif (courses[1] in dependancies):
#                 dependancies[courses[0]] = dependancies[courses[0]] + [courses[1]]
#                 course_used = course_used + 1
#             elif (courses[0] in dependancies):
#                 dependancies[courses[0]] = dependancies[courses[0]] + [courses[1]]
#                 dependancies[courses[1]] = []
#                 course_used = course_used + 1
#             else :

#         return True



        #for course in courses:
                #     print((course_used, 2))
                #     if course in dependancies:
                #         dependancies [course] = dependancies [course] + courses[:courses.index(course)]
                #         print((dependancies, 3))
                #     else:
                #         dependancies [course] = courses[:courses.index(course)]
                #         course_used = course_used + 1
                #         print((dependancies, 4))
