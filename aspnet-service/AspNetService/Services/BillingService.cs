using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using AspNetService.Models;

namespace AspNetService.Services
{
public class BillingService
{
    private readonly AppDbContext _context;

    public BillingService(AppDbContext context)
    {
        _context = context;
    }

    public async Task<List<Billing>> GetAllBillingAsync()
    {
    return await _context.Set<Billing>().ToListAsync();
    }


    public async Task<Billing> GetBillingByIdAsync(int billingId)
    {
        return await _context.Billing.FindAsync(billingId);
    }

    public async Task<Billing> CreateBillingAsync(Billing billing)
    {
        _context.Billing.Add(billing);
        await _context.SaveChangesAsync();
        return billing;
    }

    public async Task<bool> DeleteBillingAsync(int billingId)
    {
        var billing = await _context.Billing.FindAsync(billingId);
        if (billing == null)
        {
            return false;
        }

        _context.Billing.Remove(billing);
        await _context.SaveChangesAsync();
        return true;
    }
}
}