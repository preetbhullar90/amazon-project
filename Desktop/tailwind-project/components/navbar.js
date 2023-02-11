import { useState } from 'react'
import Link from 'next/link'


function NavLink({to, children}) {
    return <a href={to} className={`mx-4`}>
        {children}
    </a>
}

function MobileNav({open, setOpen}) {
    return (
        <div className={`absolute top-0 left-0  w-screen bg-white transform ${open ? "-translate-x-0" : "-translate-x-full"} transition-transform duration-300 ease-in-out filter drop-shadow-md `}>
            <div className="flex items-center justify-center filter drop-shadow-md bg-white h-20"> {/*logo container*/}
                {/* <a className="text-xl font-semibold " href="/">LOGO</a> */}
            </div>
            <div className="flex flex-col  bg-gray-700 w-94 h-[100vh] shadow-lg">
            <Link className="text-xl font-medium bg-gray-700 border-b-2 border-orange-400 px-3 py-6 text-orange-600 " href="/" onClick={() => setTimeout(() => {setOpen(!open)}, 100)}>
                    Home
                </Link>
                <Link className="text-xl font-medium  bg-gray-700 border-b-2 border-orange-400 px-3 py-6 text-orange-600 " href="/gallery" onClick={() => setTimeout(() => {setOpen(!open)}, 100)}>
                    Gallery
                </Link>
                <Link className="text-xl font-medium  bg-gray-700 border-b-2 border-orange-400 px-3 py-6 text-orange-600 " href="/contact" onClick={() => setTimeout(() => {setOpen(!open)}, 100)}>
                    Contact
                </Link>
                <Link className="text-xl font-normal  bg-gray-700 border-b-2 border-orange-400 px-3 py-6 text-orange-600 " href="/about" onClick={() => setTimeout(() => {setOpen(!open)}, 100)}>
                    About
                </Link>
            </div>  
        </div>
    )
}

export default function Navbar() {

    const [open, setOpen] = useState(false)
    return (
        <nav className="flex filter drop-shadow-md bg-white px-4 py-4 h-20 items-center">
            <MobileNav open={open} setOpen={setOpen}/>
            <div className="w-3/12 flex items-center">
                <a className="text-2xl font-semibold z-50 text-orange-400" href="/">LOGO</a>
            </div>
            <div className="w-9/12 flex justify-end items-center">

                <div className="z-50 flex relative w-8 h-8 flex-col justify-between items-center md:hidden cursor-pointer " onClick={() => {
                    setOpen(!open)
                }}>
                    {/* hamburger button */}
                    <span className={`h-1 w-full bg-orange-400 rounded-lg transform transition duration-300 ease-in-out ${open ? "rotate-45 translate-y-3.5" : ""}`} />
                    <span className={`h-1  bg-orange-400 rounded-lg transition-all duration-300 ease-in-out ${open ? "w-0" : "w-full"}`} />
                    <span className={`h-1 w-full bg-orange-400 rounded-lg transform transition duration-300 ease-in-out ${open ? "-rotate-45 -translate-y-3.5" : ""}`} />
                </div>

                <div className="hidden md:flex ">
                <div className='hover:border-b-2 text-orange-400 border-orange-500 h-8 pt-1 px-4'>

                <Link href="/" >
                        Home
                    </Link>
                </div>

                <div className='hover:border-b-2 text-orange-400 border-orange-500 h-8 pt-1 px-4'>
                    <Link href="/gallery">
                        Gallery
                    </Link>
                    </div>

                    <div className='hover:border-b-2 text-orange-400 border-orange-500 h-8 pt-1 px-4'>
                    <Link href="/contact">
                        Contact
                    </Link>
                    </div>

                    <div className='hover:border-b-2 text-orange-400 border-orange-500 h-8 pt-1 px-4'>
                    <Link href="/about">
                        About
                    </Link>
                    </div>
                </div>
            </div>
        </nav>
    )
}

    