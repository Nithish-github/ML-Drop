import { BlockType } from './BlockType';

export class Block {
  public id!: number;
  public name!: string;
  public type!: BlockType;
  public position = { x: 0, y: 0 };
}
