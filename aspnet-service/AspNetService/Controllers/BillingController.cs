using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AspNetService.Models;
using AspNetService.Services;


namespace AspNetService.Controllers
{

[Route("api/[controller]")]
[ApiController]
public class BillingController : ControllerBase
{
    private readonly AppDbContext _context;

    public BillingController(AppDbContext context)
    {
        _context = context;
    }

    // GET: api/Billing
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Billing>>> GetBilling()
    {
    return await _context.Set<Billing>().ToListAsync();
    }


    // GET: api/Billing/5
    [HttpGet("{id}")]
    public async Task<ActionResult<Billing>> GetBilling(int id)
    {
        var billing = await _context.Billing.FindAsync(id);

        if (billing == null)
        {
            return NotFound();
        }

        return billing;
    }

    // POST: api/Billing
    [HttpPost]
    public async Task<ActionResult<Billing>> PostBilling(Billing billing)
    {
        _context.Billing.Add(billing);
        await _context.SaveChangesAsync();

        return CreatedAtAction("GetBilling", new { id = billing.BillingId }, billing);
    }

    // DELETE: api/Billing/5
    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteBilling(int id)
    {
        var billing = await _context.Billing.FindAsync(id);
        if (billing == null)
        {
            return NotFound();
        }

        _context.Billing.Remove(billing);
        await _context.SaveChangesAsync();

        return NoContent();
    }
}
}