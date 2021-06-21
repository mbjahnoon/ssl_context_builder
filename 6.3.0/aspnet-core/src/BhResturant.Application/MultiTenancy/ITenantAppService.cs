using Abp.Application.Services;
using BhResturant.MultiTenancy.Dto;

namespace BhResturant.MultiTenancy
{
    public interface ITenantAppService : IAsyncCrudAppService<TenantDto, int, PagedTenantResultRequestDto, CreateTenantDto, TenantDto>
    {
    }
}

