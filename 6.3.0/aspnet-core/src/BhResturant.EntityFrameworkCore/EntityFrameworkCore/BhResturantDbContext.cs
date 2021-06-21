using Microsoft.EntityFrameworkCore;
using Abp.Zero.EntityFrameworkCore;
using BhResturant.Authorization.Roles;
using BhResturant.Authorization.Users;
using BhResturant.MultiTenancy;

namespace BhResturant.EntityFrameworkCore
{
    public class BhResturantDbContext : AbpZeroDbContext<Tenant, Role, User, BhResturantDbContext>
    {
        /* Define a DbSet for each entity of the application */
        
        public BhResturantDbContext(DbContextOptions<BhResturantDbContext> options)
            : base(options)
        {
        }
    }
}
