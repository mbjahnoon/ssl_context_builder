using System.Threading.Tasks;
using BhResturant.Configuration.Dto;

namespace BhResturant.Configuration
{
    public interface IConfigurationAppService
    {
        Task ChangeUiTheme(ChangeUiThemeInput input);
    }
}
