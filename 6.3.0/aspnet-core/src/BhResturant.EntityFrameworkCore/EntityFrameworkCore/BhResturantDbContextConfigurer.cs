using System.Data.Common;
using Microsoft.EntityFrameworkCore;

namespace BhResturant.EntityFrameworkCore
{
    public static class BhResturantDbContextConfigurer
    {
        public static void Configure(DbContextOptionsBuilder<BhResturantDbContext> builder, string connectionString)
        {
            builder.UseSqlServer(connectionString);
        }

        public static void Configure(DbContextOptionsBuilder<BhResturantDbContext> builder, DbConnection connection)
        {
            builder.UseSqlServer(connection);
        }
    }
}
