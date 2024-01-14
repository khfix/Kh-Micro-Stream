using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using AspNetService.Models;

namespace AspNetService.Services
{
public class SubscriptionService
{
    private readonly AppDbContext _context;

    public SubscriptionService(AppDbContext context)
    {
        _context = context;
    }

    public async Task<List<Subscription>> GetAllSubscriptionsAsync()
    { 
    return await _context.Set<Subscription>().ToListAsync();
    }


    public async Task<Subscription> GetSubscriptionByIdAsync(int subscriptionId)
    {
        return await _context.Subscription.FindAsync(subscriptionId);
    }

    public async Task<Subscription> CreateSubscriptionAsync(Subscription subscription)
    {
        _context.Subscription.Add(subscription);
        await _context.SaveChangesAsync();
        return subscription;
    }

    public async Task<bool> DeleteSubscriptionAsync(int subscriptionId)
    {
        var subscription = await _context.Subscription.FindAsync(subscriptionId);
        if (subscription == null)
        {
            return false;
        }

        _context.Subscription.Remove(subscription);
        await _context.SaveChangesAsync();
        return true;
    }
}
}