using System.Threading.Tasks;
using Abp.Authorization;
using Abp.Runtime.Session;
using BhResturant.Configuration.Dto;

namespace BhResturant.Configuration
{
    [AbpAuthorize]
    public class ConfigurationAppService : BhResturantAppServiceBase, IConfigurationAppService
    {
        public async Task ChangeUiTheme(ChangeUiThemeInput input)
        {
            await SettingManager.ChangeSettingForUserAsync(AbpSession.ToUserIdentifier(), AppSettingNames.UiTheme, input.Theme);
        }
    }
}
