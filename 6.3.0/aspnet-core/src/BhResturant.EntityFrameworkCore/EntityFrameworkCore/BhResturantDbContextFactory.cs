using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;
using BhResturant.Configuration;
using BhResturant.Web;

namespace BhResturant.EntityFrameworkCore
{
    /* This class is needed to run "dotnet ef ..." commands from command line on development. Not used anywhere else */
    public class BhResturantDbContextFactory : IDesignTimeDbContextFactory<BhResturantDbContext>
    {
        public BhResturantDbContext CreateDbContext(string[] args)
        {
            var builder = new DbContextOptionsBuilder<BhResturantDbContext>();
            var configuration = AppConfigurations.Get(WebContentDirectoryFinder.CalculateContentRootFolder());

            BhResturantDbContextConfigurer.Configure(builder, configuration.GetConnectionString(BhResturantConsts.ConnectionStringName));

            return new BhResturantDbContext(builder.Options);
        }
    }
}
