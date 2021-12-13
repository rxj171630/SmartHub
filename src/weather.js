import {Image,Statistic, StatisticGroup} from 'semantic-ui-react'
import React from 'react'

class WeatherComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }


  processResult(result) {
      if (!result) {
          console.log(result);
          return;
      } else {
          var res = []
          result.forEach(function (item, index) {
            res.push({name: item.weather.weatherStation, condition: item.weather.forecasts[0].condition, currentTemp: item.weather.forecasts[0].temperature, symbol: item.weather.forecasts[0].weatherSymbol, tempLow: item.weather.forecasts[0].tempLow, tempHigh: item.weather.forecasts[0].tempHigh})
          });
          return res
      }
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/weather")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: this.processResult(result)
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error: error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
          <Statistic.Group>
                  <Statistic label={`Weather Station`} value={this.state.items[0].name} />
                  <Statistic label={this.state.items[0].condition} value={<Image src={`./src/icons/0.png`}/>} />
                  <Statistic label={`Current Temp`} value={(this.state.items[0].currentTemp/ 10).toString().concat("˚F")} />
                  <Statistic label={`Low Temp`} value={(this.state.items[0].tempLow/ 10).toString().concat("˚F")} />
                  <Statistic label={`High Temp`} value={(this.state.items[0].tempHigh/ 10).toString().concat("˚F")} />
          </Statistic.Group>
      );
    }
  }
}

export default WeatherComponent
