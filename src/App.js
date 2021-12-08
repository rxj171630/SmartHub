import './App.css';
import { Header, Divider, Card, Icon, Image, Statistic, Table} from 'semantic-ui-react'
import NewsComponent from './news.js'
import StocksComponent from "./stocks.js"
import EventsComponent from "./events.js"

const StatisticGroup = () => (
  <div>
    <Statistic.Group>
      <Statistic label='Temperature' value='60˚F' />
      <Statistic label='Humidity' value='XYZ' />
    </Statistic.Group>
  </div>
)

function App() {
  return (
    <div className="App">
    <Header as='h1'>IoT Hub</Header>
    <Header as='h2' textAlign='left'>Home Statistics</Header>
    {StatisticGroup()}
    <Divider/>
    <Header as='h2' textAlign='left'>News Headlines</Header>
    <NewsComponent/>
    <Divider/>
    <Header as='h2' textAlign='left'>Stocks</Header>
    <StocksComponent/>
    <Header as='h2' textAlign='left'>Events</Header>
    <EventsComponent/>
    </div>
  );
}

export default App;
