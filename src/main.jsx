import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import 'animal-island-ui/style';
import './global.css'
import App from './App.jsx'
import {Cursor} from "animal-island-ui";

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <Cursor>
            <div
                className="
    min-h-screen
    flex
    justify-center
    bg-[#7dc395]
    bg-[url('/home_bg-CzHux1Sq.webp')]
    bg-repeat
  "
                style={{
                    animation: "bgScroll 80s linear infinite",
                }}
            >
                <App />
            </div>
        </Cursor>
    </StrictMode>,
)
