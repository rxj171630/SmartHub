import './App.css';
import { Header, Divider, Card, Icon, Image, Statistic, Table} from 'semantic-ui-react'
import NewsComponent from './news.js'
import StocksComponent from "./stocks.js"
import EventsComponent from "./events.js"
import ThermoComponent from "./thermo.js"
import HumidityComponent from "./humidity.js"
import MapsComponent from "./maps.js"
import AlarmComponent from "./alarm.js"
import NotesComponent from "./notes.js"

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

    <Header as='h2' textAlign='left'>Maps</Header>
    <MapsComponent/>
    <Divider/>

    <Header as='h2' textAlign='left'>Alarm</Header>
    <AlarmComponent/>
    <Divider/>

    <Header as='h2' textAlign='left'>Notes</Header>
    <NotesComponent/>
    <Divider/>

    </div>
  );
}

export default App;
