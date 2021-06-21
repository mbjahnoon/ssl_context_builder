using Abp.Authorization;
using BhResturant.Authorization.Roles;
using BhResturant.Authorization.Users;

namespace BhResturant.Authorization
{
    public class PermissionChecker : PermissionChecker<Role, User>
    {
        public PermissionChecker(UserManager userManager)
            : base(userManager)
        {
        }
    }
}
