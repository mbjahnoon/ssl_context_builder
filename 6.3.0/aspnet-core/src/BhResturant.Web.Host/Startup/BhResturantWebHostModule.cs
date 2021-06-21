using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Abp.Modules;
using Abp.Reflection.Extensions;
using BhResturant.Configuration;

namespace BhResturant.Web.Host.Startup
{
    [DependsOn(
       typeof(BhResturantWebCoreModule))]
    public class BhResturantWebHostModule: AbpModule
    {
        private readonly IWebHostEnvironment _env;
        private readonly IConfigurationRoot _appConfiguration;

        public BhResturantWebHostModule(IWebHostEnvironment env)
        {
            _env = env;
            _appConfiguration = env.GetAppConfiguration();
        }

        public override void Initialize()
        {
            IocManager.RegisterAssemblyByConvention(typeof(BhResturantWebHostModule).GetAssembly());
        }
    }
}
