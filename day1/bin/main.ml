[@@@warning "-8"]

open Base
module Printf = Stdlib.Printf

let goofy_regex = Pcre.regexp {|(?=([0-9]{1}|one|two|three|four|five|six|seven|eight|nine))|}

let the_array = ["one"; "two"; "three"; "four"; "five"; "six"; "seven"; "eight"; "nine"]

let rec find x lst =
  match lst with
  | [] -> raise (Failure x)
  | h :: t -> if String.equal x h then 0 else 1 + find x t

let arghh x = 
  match Int.of_string_opt x with
    | Some n -> n
    | None -> (find x the_array) + 1

let skull line =
  Pcre.full_split line ~rex:goofy_regex
  |> List.map ~f:(fun x -> match x with
    | Pcre.Group (_, x) -> x
    | _ -> "")
  |> List.filter ~f:(fun x -> not @@ String.is_empty x)

let parse_line s =
  let list = skull s
  |> List.map ~f:(fun x -> arghh x) in
  match list with
  | hd when List.length hd >= 2 -> (List.hd_exn hd, List.last_exn hd)
  | [x] -> (x, x)
  | [] -> failwith "bad input"

let () =
  let open Core in
  In_channel.read_lines "input.txt"
    |> List.map ~f:parse_line
    |> List.map ~f:(fun (t, o) -> t * 10 + o)
    |> List.map ~f:(fun x -> Printf.printf "%i\n" x; x)
    |> List.fold ~init:0 ~f:(fun acc n -> acc + n)
    |> (fun x -> Printf.printf "%i\n" x)