# React Chat Widget

A clean, modern React component for embedding the AI chatbot in your portfolio.

## Installation

1. Copy `ChatWidget.jsx` and `ChatWidget.module.css` to your React project:
   ```
   src/components/ChatWidget/
   ├── ChatWidget.jsx
   └── ChatWidget.module.css
   ```

2. Import and use in your portfolio:
   ```jsx
   import ChatWidget from './components/ChatWidget/ChatWidget';

   export default function Portfolio() {
     return (
       <div>
         <h1>My Portfolio</h1>
         {/* For local development */}
         <ChatWidget apiUrl="http://localhost:5000" />
         
         {/* For production - update URL to your deployed backend */}
         {/* <ChatWidget apiUrl="https://your-chatbot-api.com" /> */}
       </div>
     );
   }
   ```

## Features

- ✅ Clean, modern UI with gradient header
- ✅ Real-time message updates
- ✅ Auto-scrolling to latest message
- ✅ Loading state with animated dots
- ✅ Responsive design
- ✅ Error handling
- ✅ Auto-initializes conversation on mount
- ✅ Persistent conversation across refreshes

## Customization

### Change API URL
```jsx
<ChatWidget apiUrl="https://your-deployed-api.com" />
```

### Customize Colors
Edit `ChatWidget.module.css`:
- Change `#667eea` to your primary color
- Change `#764ba2` to your secondary color

### Adjust Size
```jsx
<div style={{ maxWidth: '500px' }}>
  <ChatWidget apiUrl="http://localhost:5000" />
</div>
```

## Environment Variables (Optional)

In your portfolio's `.env`:
```
REACT_APP_CHATBOT_API=http://localhost:5000
```

Then in your component:
```jsx
<ChatWidget apiUrl={process.env.REACT_APP_CHATBOT_API} />
```

## Deployment Notes

1. **Local Development**: API runs on `http://localhost:5000`
2. **Production**: Deploy backend to Render/Railway and update `apiUrl`
3. **CORS**: Already enabled in Flask backend

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)
