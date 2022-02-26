peoplelist = {}
names = []
ability = []
current0 = []
projectnames = []

people, projects = map(int, input().split())
for i in range(people):
    name, skills = map(str, input().split())
    names.append(name)

    skills = int(skills)
    for y in range(skills):
        lang, level = map(str, input().split())
        current0.append((lang, level))
    peoplelist[names[i]] = [current0, True]  # looks like name:[(lang,level),(lang,level)]
    current0 = []
roles = []
projectset = []

projectpara = []
projectlist = {}  # looks like projectname: [(days,score,bestbefore,roles),[(c++,3),(html,5)]]
for j in range(projects):
    project, D, S, B, R = map(str, input().split())
    D = int(D)
    S = int(S)
    B = int(B)
    R = int(R)
    projectnames.append(project)
    projectpara.append((project, D, S, B, R))
    for x in range(R):
        skill, level = map(str, input().split())
        roles.append((skill, level))
        # print(roles)
    projectset.append((roles))
    roles = []
# print(projectset, len(projectset))

for i in range(projects):
    current = projectpara[i]
    projectlist[current[0]] = [(current[1], current[2], current[3], current[4]), (projectset[i])]
    # for i in range(people):
    # current2 = names[i]
    # peoplelist[current2] = [(current2[1], current2[2], current2[3]), (ability[i])]
    #the;


# an item in the dictionary looks like: project :[(DSBR), [(c++,3),(html,2)]]


# print(projectlist, peoplelist)
# an item in the dictionary looks like: project :[(DSBR), [(c++,3),(html,2)]]


class Project:

    def __init__(self, name, D, S, B,
                 roles):  # assuming days, score, bb is int, roles is array, maybe of tupes e.g. [(c++,3),(python,2)]
        self.DAYS = D
        self.SCORE = S
        self.BB = B
        self.ROLES = roles
        self.POINTS_PER_DAY = S / D
        self.EVAL = S / (D * len(roles))
        self.NAME = name


project_objects = []
proj = 0
for i in range(len(projectset)):
    # print(f'i={i}')
    name = projectnames[i]
    proj = projectlist[name]

    project_objects.append(Project(name, proj[0][0], proj[0][1], proj[0][2], proj[1]))


def eval_proj(project):
    return project.EVAL


project_objects.sort(reverse=True, key=eval_proj)


def suitability(project):
    roles = project.ROLES
    # print(roles)
    finallist = []
    eligible = ('&')
    bench = 90
    index = 0
    for i in roles:
        # print(f'role={i}')
        bench = 90
        for name in names:
            person = peoplelist[name]
            # print(name)
            if person[1] != True:
                pass
            elif True:
                for j in range(len(person[0])):
                    if i[0] == person[0][j][0] and person[0][j][1] >= i[1]:
                        if int(person[0][j][1]) < bench:
                            eligible = name
                            bench = int(person[0][j][1])
                            person[1] = False
                            # print(f'{name} was accepted')

        finallist.append(eligible)
        if eligible == '&':
            return False
        eligible = '&'

    return finallist


day = 0
possibleprojects = []
# print(project_objects[0].NAME)
# print(suitability(project_objects[0]))
for project in project_objects:
    # print(suitability(project),project.NAME)
    if suitability(project) != False:
        possibleprojects.append((project.NAME, suitability(project)))
        day += project.DAYS
        if suitability(project) != False:
            for i in suitability(project):
                peoplelist[i][1] = True

namey = ''
print(len(possibleprojects))
for i in range(len(possibleprojects)):
    namey = ''
    print(possibleprojects[i][0])
    if possibleprojects[i][1] != False:
        for j in range(len(possibleprojects[i][1])):
            possibleprojects[i][1][j] += ' '
            namey += possibleprojects[i][1][j]
        print(namey)
