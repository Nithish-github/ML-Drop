import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Block } from '../models/block';
import { BlockType } from '../models/BlockType';
import { jsPlumb, jsPlumbInstance } from 'jsplumb';

@Injectable({
  providedIn: 'root',
})
export class BlockManagerService {
  constructor() {}

  public blockCount: number = 0;

  public blockList: Block[] = [];

  public $isBlockUpdateAvailable: BehaviorSubject<boolean> =
    new BehaviorSubject(false);

  public $isNewBlockPushed: BehaviorSubject<boolean> = new BehaviorSubject(
    false
  );

  private jsPlumbInstance = jsPlumb.getInstance({
    Connector: 'Straight',
    Endpoint: 'Dot',
    Anchor: 'Continuous',
    PaintStyle: { stroke: 'black', strokeWidth: 10 },
  });

  public addBlock() {
    const block: Block = {
      id: this.blockCount + 1,
      name: this.blockCount + 1 + 'Block',
      position: { x: 0, y: 0 },
      type: BlockType.Image_Block,
    };
    this.blockList.push(block);
    this.$isBlockUpdateAvailable.next(true);
  }

  public deleteAllBlocks() {
    this.blockList = [];
    this.$isBlockUpdateAvailable.next(true);
  }

  public getJsPlumbInstance(): jsPlumbInstance {
    return this.jsPlumbInstance;
  }
}
