using Abp.AspNetCore;
using Abp.AspNetCore.TestBase;
using Abp.Modules;
using Abp.Reflection.Extensions;
using BhResturant.EntityFrameworkCore;
using BhResturant.Web.Startup;
using Microsoft.AspNetCore.Mvc.ApplicationParts;

namespace BhResturant.Web.Tests
{
    [DependsOn(
        typeof(BhResturantWebMvcModule),
        typeof(AbpAspNetCoreTestBaseModule)
    )]
    public class BhResturantWebTestModule : AbpModule
    {
        public BhResturantWebTestModule(BhResturantEntityFrameworkModule abpProjectNameEntityFrameworkModule)
        {
            abpProjectNameEntityFrameworkModule.SkipDbContextRegistration = true;
        } 
        
        public override void PreInitialize()
        {
            Configuration.UnitOfWork.IsTransactional = false; //EF Core InMemory DB does not support transactions.
        }

        public override void Initialize()
        {
            IocManager.RegisterAssemblyByConvention(typeof(BhResturantWebTestModule).GetAssembly());
        }
        
        public override void PostInitialize()
        {
            IocManager.Resolve<ApplicationPartManager>()
                .AddApplicationPartsIfNotAddedBefore(typeof(BhResturantWebMvcModule).Assembly);
        }
    }
}