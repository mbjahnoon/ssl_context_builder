using System.Threading.Tasks;
using BhResturant.Models.TokenAuth;
using BhResturant.Web.Controllers;
using Shouldly;
using Xunit;

namespace BhResturant.Web.Tests.Controllers
{
    public class HomeController_Tests: BhResturantWebTestBase
    {
        [Fact]
        public async Task Index_Test()
        {
            await AuthenticateAsync(null, new AuthenticateModel
            {
                UserNameOrEmailAddress = "admin",
                Password = "123qwe"
            });

            //Act
            var response = await GetResponseAsStringAsync(
                GetUrl<HomeController>(nameof(HomeController.Index))
            );

            //Assert
            response.ShouldNotBeNullOrEmpty();
        }
    }
}