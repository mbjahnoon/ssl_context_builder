using Abp.AutoMapper;
using Abp.Modules;
using Abp.Reflection.Extensions;
using BhResturant.Authorization;

namespace BhResturant
{
    [DependsOn(
        typeof(BhResturantCoreModule), 
        typeof(AbpAutoMapperModule))]
    public class BhResturantApplicationModule : AbpModule
    {
        public override void PreInitialize()
        {
            Configuration.Authorization.Providers.Add<BhResturantAuthorizationProvider>();
        }

        public override void Initialize()
        {
            var thisAssembly = typeof(BhResturantApplicationModule).GetAssembly();

            IocManager.RegisterAssemblyByConvention(thisAssembly);

            Configuration.Modules.AbpAutoMapper().Configurators.Add(
                // Scan the assembly for classes which inherit from AutoMapper.Profile
                cfg => cfg.AddMaps(thisAssembly)
            );
        }
    }
}
