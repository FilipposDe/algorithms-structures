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



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if type(user) is not str or type(group) is not Group:
        return False

    if user in group.get_users():
        return True
        
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True

    return False


########################################################
##                      TEST CASES                    ##
########################################################
## Note: Working directory is 'testdir'
print("\n\n___ TEST 1 ___")

g_1 = Group("1")
g_1_a = Group("1a")
g_1.add_group(g_1_a)
g_1_b = Group("1b")
g_1.add_group(g_1_b)
g_1_b_i = Group("1bi")
g_1_b.add_group(g_1_b_i)
g_1_b_ii = Group("1bii")
g_1_b.add_group(g_1_b_ii)

user = "user1"
g_1_b_ii.add_user(user)

print(is_user_in_group(user, g_1))
# Expected True

print(is_user_in_group(user, g_1_b_ii))
# Expected True

print(is_user_in_group(user, g_1_b_i))
# Expected False


print("\n\n___ TEST 2 ___")
print(is_user_in_group(111, ''))
# Expected False


print("\n\n___ TEST 3 ___")
print(is_user_in_group('user2', g_1))
# Expected False






# parent = Group("parent")
# child = Group("child")
# sub_child = Group("subchild")

# sub_child_user = "sub_child_user"
# sub_child.add_user(sub_child_user)

# child.add_group(sub_child)
# parent.add_group(child)
