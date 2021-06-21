using Abp.AspNetCore.Mvc.Controllers;
using Abp.IdentityFramework;
using Microsoft.AspNetCore.Identity;

namespace BhResturant.Controllers
{
    public abstract class BhResturantControllerBase: AbpController
    {
        protected BhResturantControllerBase()
        {
            LocalizationSourceName = BhResturantConsts.LocalizationSourceName;
        }

        protected void CheckErrors(IdentityResult identityResult)
        {
            identityResult.CheckErrors(LocalizationManager);
        }
    }
}
