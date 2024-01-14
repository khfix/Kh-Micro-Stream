using Microsoft.EntityFrameworkCore;

namespace AspNetService.Models
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        public DbSet<Billing> Billing { get; set; }
        public DbSet<Subscription> Subscription { get; set; }
    }
}
