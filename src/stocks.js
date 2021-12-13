import {Table} from 'semantic-ui-react'
import React from 'react'

class StocksComponent extends React.Component {
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
          result.quoteResponse.result.forEach(function (item, index) {
            res.push({name: item.shortName, symbol: item.symbol, ask: item.ask, bid: item.bid, marketCap: item.marketCap})
          });
          return res;
      }
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/stocks")
    .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: this.processResult(result)
          });
        },
        (error) => {
            console.log(error);
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
          <Table celled>
            <Table.Header>
              <Table.Row>
                <Table.HeaderCell>Short Name</Table.HeaderCell>
                <Table.HeaderCell>Ticker Symbol</Table.HeaderCell>
                <Table.HeaderCell>Bid</Table.HeaderCell>
                <Table.HeaderCell>Ask</Table.HeaderCell>
                <Table.HeaderCell>Market Cap</Table.HeaderCell>
              </Table.Row>
            </Table.Header>

            <Table.Body>
            {this.state.items.map(( val, index ) => {
                return (
                    <Table.Row key={index}>
                      <Table.Cell>{val.name}</Table.Cell>
                      <Table.Cell>{val.symbol}</Table.Cell>
                      <Table.Cell>{val.bid}</Table.Cell>
                      <Table.Cell>{val.ask}</Table.Cell>
                      <Table.Cell>{val.marketCap}</Table.Cell>
                    </Table.Row>
                );
            })}
            </Table.Body>
            </Table>
      );
    }
  }
}

export default StocksComponent
