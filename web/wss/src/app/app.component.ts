import { Component } from '@angular/core';
import { Observer, Observable } from 'rxjs';
import { environment } from '../environments/environment';
import { PushReport } from './types/api_push_report';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent {

  public connectReport?: PushReport;
  public updateReport?: PushReport;
  public contentVisible: boolean = false;

  private initObserver?: Observer<void> = undefined;
  private wsEndpoint: string = "";
  private websocket?: WebSocket = undefined;

  constructor() {
    this.wsEndpoint = `${window.location.protocol.replace("http", "ws")}//${environment.api_host}${environment.api_port ? ":" + environment.api_port : ""}/ws`
    console.log(`wsEndpoint: ${this.wsEndpoint}`)
    new Observable((observer) => {
      this.initObserver = observer;
    }).subscribe(() => {
      this.ready();
    })
  }

  public ngOnInit(): void {
    this.websocket = new WebSocket(this.wsEndpoint);
    this.websocket.onopen = () => {
      if (this.websocket) {
        this.websocket.onmessage = arg => {

          this.pushReceived(arg.data);
        };
      }
      if (this.initObserver) {
        this.initObserver.next();
        this.initObserver.complete();
      }
    };
  }

  public buttonClicked(): void {
    this.sendMessage("client button clicked")
  }

  private sendMessage(message: string): void {
    if (this.websocket) {
      this.websocket.send(message)
    }
  }

  private ready(): void {
    this.contentVisible = true;
  }

  private pushReceived(arg: string): void {
    const parsed = JSON.parse(arg);
    switch (parsed.push_type) {
      case "connected_to":
        this.connectReport = parsed;
        break;
      case "notified_by":
        this.updateReport = parsed;
        break;
    }
  }
}
