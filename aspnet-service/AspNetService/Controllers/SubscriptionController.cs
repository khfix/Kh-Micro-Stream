using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AspNetService.Models;
using AspNetService.Models;



namespace AspNetService.Controllers
{
[Route("api/[controller]")]
[ApiController]
public class SubscriptionController : ControllerBase
{
    private readonly AppDbContext _context;

    public SubscriptionController(AppDbContext context)
    {
        _context = context;
    }

    // GET: api/Subscription
   [HttpGet]
   public async Task<ActionResult<IEnumerable<Subscription>>> GetSubscription()
   {
     return await _context.Set<Subscription>().ToListAsync();
   }


    // GET: api/Subscription/5
    [HttpGet("{id}")]
    public async Task<ActionResult<Subscription>> GetSubscription(int id)
    {
        var subscription = await _context.Subscription.FindAsync(id);

        if (subscription == null)
        {
            return NotFound();
        }

        return subscription;
    }

    // POST: api/Subscription
    [HttpPost]
    public async Task<ActionResult<Subscription>> PostSubscription(Subscription subscription)
    {
        _context.Subscription.Add(subscription);
        await _context.SaveChangesAsync();

        return CreatedAtAction("GetSubscription", new { id = subscription.SubscriptionId }, subscription);
    }

    // DELETE: api/Subscription/5
    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteSubscription(int id)
    {
        var subscription = await _context.Subscription.FindAsync(id);
        if (subscription == null)
        {
            return NotFound();
        }

        _context.Subscription.Remove(subscription);
        await _context.SaveChangesAsync();

        return NoContent();
    }
}
}
