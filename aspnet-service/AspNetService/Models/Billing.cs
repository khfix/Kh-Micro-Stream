
namespace AspNetService.Models;
public class Billing
{
    public int BillingId { get; set; }
    public int UserId { get; set; }
    public decimal Amount { get; set; }
    public DateTime Timestamp { get; set; }
}
