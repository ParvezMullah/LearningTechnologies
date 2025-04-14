import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const Card = ({title}) => {
  const [count, setCount] = useState(0)
  const [hasLiked, setHasLiked] = useState(false);

  useEffect(() => {
    console.log(`${title} has been liked: ${hasLiked}`);
  }, [title, hasLiked]);

  return (
    <div>
      <h2>{title} - {count}</h2>
      <button onClick={() => setCount(count+1)}>
        {hasLiked ? 'Liked': 'Like'}
      </button>
    </div>
  )
}

const App = () => {
  return (
    <div className='card-container'>
      <h2>Functional Arrow Component</h2>
      <Card title="Star Wars" />
      <Card title="Avatar" />
      <Card title="The Lion King" />
    </div>
  )
}

export default App
