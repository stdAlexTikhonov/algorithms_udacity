class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



parent = Group("parent")
child = Group("child")
child2 = Group('child2')
sub_child2 = Group('sub_child2')
sub_child3 = Group('sub_child3')
sub_child3.add_user('mama')

sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
child2.add_group(sub_child2)
child2.add_group(sub_child3)

parent.add_group(child)
parent.add_group(child2)


def is_user_in_group(start, user):
    if user and start:
        result = []
        if start is None:
            return None
        
        current_path = str(start.name)

        if len(start.groups) == 0:
            result.append(current_path)
            if user in start.get_users():
                return True
            else:
                return False
        elif user in start.get_users():
            return True
        else:
            i = 0
            len_nodes = len(start.groups)
            while i < len_nodes:
                if dfs(start.groups[i], current_path, result, user):
                    return True
                i+=1
    else:
        if user:
            return "Group is not specified"
        elif start:
            return "User is not specified"
        else:
            return "Both user and group are not specified"
        

    return "User '{}' not found".format(user)

def dfs(node, current_path, result, user):
    current_path += '-> ' + str(node.name)

    if len(node.groups) == 0:
        result.append(current_path)
        if user in node.get_users():
            return True
        else:
            return False
    elif user in node.get_users():
        return True
    else:
        i = 0
        len_nodes = len(node.groups)
        while i < len_nodes:
            if dfs(node.groups[i], current_path, result, user):
                return True
            i+=1


#Test
print(is_user_in_group(parent, 'mama'))

#Test user not found
print(is_user_in_group(parent, 'dada'))

#Test empty string
print(is_user_in_group(parent, ''))

#Test empty group
print(is_user_in_group(None, 'User'))