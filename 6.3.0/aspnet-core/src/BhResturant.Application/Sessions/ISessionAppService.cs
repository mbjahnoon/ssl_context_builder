using System.Threading.Tasks;
using Abp.Application.Services;
using BhResturant.Sessions.Dto;

namespace BhResturant.Sessions
{
    public interface ISessionAppService : IApplicationService
    {
        Task<GetCurrentLoginInformationsOutput> GetCurrentLoginInformations();
    }
}
