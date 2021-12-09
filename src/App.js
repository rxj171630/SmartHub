import './App.css';
import { Header, Divider, Card, Icon, Image, Statistic, Table} from 'semantic-ui-react'
import NewsComponent from './news.js'
import StocksComponent from "./stocks.js"
import EventsComponent from "./events.js"
import ThermoComponent from "./thermo.js"
import HumidityComponent from "./humidity.js"

function App() {
  return (
    <div className="App">
    <Header as='h1'>IoT Hub</Header>
    <Divider/>

    <Header as='h2' textAlign='left'>Thermo</Header>
    <ThermoComponent/>
    <Divider/>

    <Header as='h2' textAlign='left'>Humidity</Header>
    <HumidityComponent/>
    <Divider/>

    <Header as='h2' textAlign='left'>News Headlines</Header>
    <NewsComponent/>
    <Divider/>

    <Header as='h2' textAlign='left'>Stocks</Header>
    <StocksComponent/>
    <Divider/>

    <Header as='h2' textAlign='left'>Events</Header>
    <EventsComponent/>
    <Divider/>

    </div>
  );
}

export default App;
