
namespace AspNetService.Models;
public class Subscription
{
    public int SubscriptionId { get; set; }
    public int UserId { get; set; }
    public string PlanType { get; set; } = "";
    public DateTime StartDate { get; set; }
    public DateTime EndDate { get; set; }
}
