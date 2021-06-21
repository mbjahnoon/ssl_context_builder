using System.ComponentModel.DataAnnotations;

namespace BhResturant.Users.Dto
{
    public class ChangeUserLanguageDto
    {
        [Required]
        public string LanguageName { get; set; }
    }
}