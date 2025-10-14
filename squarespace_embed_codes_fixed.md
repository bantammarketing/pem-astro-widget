# Squarespace Embed Codes - Fixed for CORS Issues

## Problem
Squarespace often blocks `raw.githubusercontent.com` URLs due to CORS policies and security restrictions.

## Solutions

### Solution 1: Direct HTML Embed (Recommended)
Instead of using iframes, copy the entire HTML content directly into a Code block:

#### Wags Tecumseh Store
```html
<style>
  #astro-deals-grid {
    width: 100%;
    margin: 0 auto;
  }
  .deals-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1em;
    width: 100%;
  }
  .deal-card {
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 1em;
    background: #fff;
    box-sizing: border-box;
  }
  .deal-card img {
    max-width: 100%;
    border-radius: 4px;
    display: block;
    margin: 0 auto 0.5em auto;
  }
  .deal-title {
    font-weight: bold;
    margin-bottom: 0.5em;
  }
  .deal-expiration {
    color: #888;
    font-size: 0.9em;
  }
  .deal-brand {
    color: #555;
    font-size: 1em;
    margin-bottom: 0.5em;
  }
</style>
<div id="astro-deals-grid"></div>
<script>
fetch('https://raw.githubusercontent.com/bantammarketing/pem-astro-widget/main/deals_wags_tecumseh.json')
  .then(res => res.json())
  .then(deals => {
    const grid = document.getElementById('astro-deals-grid');
    grid.innerHTML = `
      <div class="deals-grid">
        ${deals.map(deal => `
          <div class="deal-card">
            ${deal.image ? `<img src="${deal.image}" alt="${deal.title}">` : ''}
            <div class="deal-brand">${deal.brand}</div>
            <div class="deal-title">${deal.title}</div>
            ${deal.validity ? `<div class="deal-expiration">Valid: ${deal.validity}</div>` : ''}
          </div>
        `).join('')}
      </div>
    `;
  })
  .catch(() => {
    document.getElementById('astro-deals-grid').innerHTML = "<p>Could not load deals.</p>";
  });
</script>
```

#### Pet Supplies Escondido Store
```html
<style>
  #astro-deals-grid {
    width: 100%;
    margin: 0 auto;
  }
  .deals-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1em;
    width: 100%;
  }
  .deal-card {
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 1em;
    background: #fff;
    box-sizing: border-box;
  }
  .deal-card img {
    max-width: 100%;
    border-radius: 4px;
    display: block;
    margin: 0 auto 0.5em auto;
  }
  .deal-title {
    font-weight: bold;
    margin-bottom: 0.5em;
  }
  .deal-expiration {
    color: #888;
    font-size: 0.9em;
  }
  .deal-brand {
    color: #555;
    font-size: 1em;
    margin-bottom: 0.5em;
  }
</style>
<div id="astro-deals-grid"></div>
<script>
fetch('https://raw.githubusercontent.com/bantammarketing/pem-astro-widget/main/deals_pet_supplies_escondido.json')
  .then(res => res.json())
  .then(deals => {
    const grid = document.getElementById('astro-deals-grid');
    grid.innerHTML = `
      <div class="deals-grid">
        ${deals.map(deal => `
          <div class="deal-card">
            ${deal.image ? `<img src="${deal.image}" alt="${deal.title}">` : ''}
            <div class="deal-brand">${deal.brand}</div>
            <div class="deal-title">${deal.title}</div>
            ${deal.validity ? `<div class="deal-expiration">Valid: ${deal.validity}</div>` : ''}
          </div>
        `).join('')}
      </div>
    `;
  })
  .catch(() => {
    document.getElementById('astro-deals-grid').innerHTML = "<p>Could not load deals.</p>";
  });
</script>
```

#### Tru Pet Richmond Hill Store
```html
<style>
  #astro-deals-grid {
    width: 100%;
    margin: 0 auto;
  }
  .deals-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1em;
    width: 100%;
  }
  .deal-card {
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 1em;
    background: #fff;
    box-sizing: border-box;
  }
  .deal-card img {
    max-width: 100%;
    border-radius: 4px;
    display: block;
    margin: 0 auto 0.5em auto;
  }
  .deal-title {
    font-weight: bold;
    margin-bottom: 0.5em;
  }
  .deal-expiration {
    color: #888;
    font-size: 0.9em;
  }
  .deal-brand {
    color: #555;
    font-size: 1em;
    margin-bottom: 0.5em;
  }
</style>
<div id="astro-deals-grid"></div>
<script>
fetch('https://raw.githubusercontent.com/bantammarketing/pem-astro-widget/main/deals_tru_pet_richmond_hill.json')
  .then(res => res.json())
  .then(deals => {
    const grid = document.getElementById('astro-deals-grid');
    grid.innerHTML = `
      <div class="deals-grid">
        ${deals.map(deal => `
          <div class="deal-card">
            ${deal.image ? `<img src="${deal.image}" alt="${deal.title}">` : ''}
            <div class="deal-brand">${deal.brand}</div>
            <div class="deal-title">${deal.title}</div>
            ${deal.validity ? `<div class="deal-expiration">Valid: ${deal.validity}</div>` : ''}
          </div>
        `).join('')}
      </div>
    `;
  })
  .catch(() => {
    document.getElementById('astro-deals-grid').innerHTML = "<p>Could not load deals.</p>";
  });
</script>
```

### Solution 2: Alternative iframe with different approach
If you prefer to use iframes, try this approach:

```html
<div style="width: 100%; height: 800px; overflow: hidden;">
  <iframe 
    src="https://raw.githubusercontent.com/bantammarketing/pem-astro-widget/main/widget_tecumseh.html" 
    width="100%" 
    height="100%" 
    frameborder="0" 
    scrolling="auto"
    style="border: none; transform: scale(1); transform-origin: top left;">
  </iframe>
</div>
```

### Solution 3: Use a CORS Proxy (Temporary)
If the above doesn't work, you can use a CORS proxy:

```html
<script>
fetch('https://cors-anywhere.herokuapp.com/https://raw.githubusercontent.com/bantammarketing/pem-astro-widget/main/deals_wags_tecumseh.json')
  .then(res => res.json())
  .then(deals => {
    // ... rest of the code
  });
</script>
```

## Instructions for Squarespace

1. **Go to your Squarespace page editor**
2. **Add a "Code" block** (not Embed block)
3. **Paste the entire HTML code** from Solution 1 above
4. **Save and publish**

## Troubleshooting

- Make sure you're using a **Code block**, not an **Embed block**
- Test in different browsers
- Check browser console for any JavaScript errors
- Ensure your Squarespace site is using HTTPS

## Alternative: GitHub Pages Setup

For a more permanent solution, we can set up GitHub Pages:
1. Go to your repository settings
2. Enable GitHub Pages
3. Use the GitHub Pages URL instead of raw.githubusercontent.com
