import {Statistic, StatisticGroup} from 'semantic-ui-react'
import React from 'react'

class ThermoComponent extends React.Component {
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
            res.push({name: item.name, temp: item.runtime.actualTemperature, humidity: item.runtime.actualHumidity})
          });
          return res
      }
  }

  componentDidMount() {
    fetch("http://192.168.86.41:8000/thermo")
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
          {this.state.items.map(( val, index ) => {
              return (
                  <Statistic label={val.name} value={(val.temp / 10).toString().concat("˚F")} />
                  // <Statistic label='Humidity' value={val.humidity} />
              );
          })}
          </Statistic.Group>
      );
    }
  }
}

export default ThermoComponent
