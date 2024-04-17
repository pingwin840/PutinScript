def PutinScript(commands):
    result = ''
    for command in commands:
        cmd, args = command.split(':')
        args = args.split()

        if cmd.strip() == 'Важно не то, сколько у нас будет статей':
            result += str(len(args)) + '\n'
        elif cmd.strip() == 'Все должно быть сбалансировано':
            result += str(sum(map(int, args)) / len(args)) + '\n'
        elif cmd.strip() == 'Повторить как попугай':
            result += ' '.join(args * 2) + '\n'
        elif cmd.strip() == 'Сколько людей, столько и мнений':
            result += ' '.join(set(args)) + '\n'
        elif cmd.strip() == 'Терпение и труд все перетрут':
            result += (args[1] + ' ') * int(args[0]) + '\n'
        elif cmd.strip() == 'Береги платье снову, а честь смолоду':
            result += ' '.join(sorted(args)) + '\n'
        elif cmd.strip() == 'Кто в лес, кто по дрова':
            result += ' '.join(args) + '\n'
        elif cmd.strip() == 'А вы прямо таки вангуете':
            result += str(int(args[0])) + '\n'
        elif cmd.strip() == 'Быть или не быть':
            result += ' '.join(args).upper() + '\n'
        elif cmd.strip() == 'Подумайте сами, решайте сами':
            result += ' '.join(args[::-1]) + '\n'
        elif cmd.strip() == 'Все в ваших руках':
            result += str(max(map(int, args))) + '\n'
        elif cmd.strip() == 'Никогда не сдавайся':
            result += str(min(map(int, args))) + '\n'
        elif cmd.strip() == 'Все возвращается на круги своя':
            result += ' '.join(args).title() + '\n'
        elif cmd.strip() == 'Сложнее всего начать действовать':
            result += ' '.join(args).lower() + 'n'
        elif cmd.strip() == 'Сделай шаг, и дорога появится сама собой':
            result += ' '.join(sorted(args, key=len)) + 'n'
        elif cmd.strip() == 'Успех - это способность переходить от одной неудачи к другой без потери энтузиазма':
            result += str(sum([int(i) for i in args if i.isdigit()])) + 'n'
        elif cmd.strip() == 'Не бойся совершенства, тебе его никогда не достичь':
            result += ' '.join(args).replace(' ','') + 'n'
        elif cmd.strip() == 'Всегда выбирайте самый трудный путь - на нем вы не встретите конкурентов':
            result += ' '.join([str(len(i)) for i in args]) + 'n'
        elif cmd.strip() == 'Время - лучший лекарь':
            result += ' '.join(sorted(args, key=int)) + 'n'
        elif cmd.strip() == 'Без труда не выловишь и рыбку из пруда':
            result += ' '.join(sorted(args, reverse=True, key=int)) + 'n'
        elif cmd.strip() == 'Нет худа без добра':
            result += str(sum([int(i)**2 for i in args if i.isdigit()])) + 'n'
        elif cmd.strip() == 'Семь раз отмерь, один раз отрежь':
            result += ' '.join([i for i in args if i.isalpha()]) + 'n'
        elif cmd.strip() == 'Кто рано встает, тому Бог дает':
            result += ' '.join([i for i in args if not i.isalpha()]) + 'n'
        else:
            result += 'Путину не нравится ваш код' + 'n'
    return result
