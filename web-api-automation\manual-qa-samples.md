# Manual QA samples

## Test scenario: guest checkout
**ID:** WEB-CHECKOUT-001  
**Precondition:** User is signed in to the demo store and the inventory page is loaded.

| Step | Action | Expected result |
|---|---|---|
| 1 | Add an available item to cart | Cart badge increments to 1 |
| 2 | Open cart and select Checkout | Customer information form appears |
| 3 | Submit first name, last name and postal code | Order overview is displayed |
| 4 | Finish checkout | Confirmation heading is shown |

**Risk:** High. Checkout is a primary revenue path.  
**Test data:** Standard demo account; synthetic customer details only.

## Sample bug report
**Title:** Checkout accepts a blank postal code  
**Environment:** Desktop Chrome, demo store  
**Severity:** Medium · **Priority:** High  
**Steps:** Add an item → Checkout → enter first and last name → leave postal code blank → Continue.  
**Expected:** Inline validation explains that postal code is required.  
**Actual:** The checkout advances to the order overview.  
**Evidence:** Attach a screenshot and browser trace from a reproducible run.

This is a portfolio example, not a claim about a live product defect. Verify behavior before filing against any real product.
